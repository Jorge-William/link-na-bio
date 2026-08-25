import { parseHost } from "@linknabio/shared";

export interface Env {
  HOST_MAP: KVNamespace;
  SITES: R2Bucket;
  SERVICE_NAME: string;
  SITES_ZONE: string;
  PLATFORM_ZONE: string;
}

interface HostMapEntry {
  tenantId: string;
  status: "live" | "paused_billing" | "paused_inactivity" | "draft";
  plan: string;
  prefix: string;
}

function html(body: string, status = 200): Response {
  return new Response(body, {
    status,
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "public, max-age=60",
    },
  });
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === "/health") {
      return Response.json({
        ok: true,
        service: env.SERVICE_NAME,
        ts: new Date().toISOString(),
      });
    }

    const host = request.headers.get("Host") ?? url.host;
    const lookup = parseHost(host, env.SITES_ZONE, env.PLATFORM_ZONE);

    if (lookup.kind === "unknown") {
      return html(platformHint(env.SITES_ZONE), 404);
    }

    const mapKey =
      lookup.kind === "platform_slug"
        ? `slug:${lookup.slug}`
        : `host:${lookup.hostname}`;

    const raw = await env.HOST_MAP.get(mapKey);
    if (!raw) {
      // F0: sem tenant — página amigável (UC-52)
      return html(notFoundPage(host), 404);
    }

    let entry: HostMapEntry;
    try {
      entry = JSON.parse(raw) as HostMapEntry;
    } catch {
      return html(notFoundPage(host), 404);
    }

    if (
      entry.status === "paused_billing" ||
      entry.status === "paused_inactivity"
    ) {
      return html(pausedPage(entry.status), 200);
    }

    if (entry.status !== "live") {
      return html(notFoundPage(host), 404);
    }

    const path =
      url.pathname === "/" ? "/index.html" : url.pathname;
    const key = `${entry.prefix.replace(/\/$/, "")}${path}`;
    const obj = await env.SITES.get(key);

    if (!obj) {
      return html(notFoundPage(host), 404);
    }

    const headers = new Headers();
    obj.writeHttpMetadata(headers);
    headers.set("etag", obj.httpEtag);
    headers.set("Cache-Control", "public, max-age=300");

    return new Response(obj.body, { headers });
  },
} satisfies ExportedHandler<Env>;

function notFoundPage(host: string): string {
  return `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Não encontrado</title>
<style>body{font-family:system-ui;display:grid;place-items:center;min-height:100vh;margin:0;color:#0f172a}
main{text-align:center;padding:2rem}code{background:#f1f5f9;padding:.2rem .4rem;border-radius:4px}</style></head>
<body><main><h1>Site não encontrado</h1><p>Nenhum tenant para <code>${escapeHtml(host)}</code>.</p></main></body></html>`;
}

function pausedPage(reason: string): string {
  return `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"/><title>Assinatura pausada</title>
<style>body{font-family:system-ui;display:grid;place-items:center;min-height:100vh;margin:0}
main{max-width:28rem;text-align:center;padding:2rem}</style></head>
<body><main><h1>Assinatura pausada</h1><p>Este site está temporariamente indisponível (${escapeHtml(reason)}).</p>
<p>Dono: entre no app para regularizar.</p></main></body></html>`;
}

function platformHint(sitesZone: string): string {
  return `<!DOCTYPE html><html lang="pt-BR"><head><meta charset="utf-8"/><title>sites</title></head>
<body style="font-family:system-ui;padding:2rem"><h1>Worker sites</h1>
<p>Use <code>{slug}.${escapeHtml(sitesZone)}</code> ou domínio custom.</p>
<p><a href="/health">/health</a></p></body></html>`;
}

function escapeHtml(s: string): string {
  return s
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}
