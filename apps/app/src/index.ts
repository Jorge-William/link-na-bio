import { featuresFor, type PlanId } from "@linknabio/shared";

export interface Env {
  DB: D1Database;
  HOST_MAP: KVNamespace;
  SITES: R2Bucket;
  PUBLISH: Queue;
  SERVICE_NAME: string;
  SITES_ZONE: string;
  PLATFORM_ZONE: string;
}

const CORS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type, Authorization",
};

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json", ...CORS },
  });
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: CORS });
    }

    const url = new URL(request.url);

    if (url.pathname === "/health") {
      let dbOk = false;
      try {
        await env.DB.prepare("SELECT 1 AS ok").first();
        dbOk = true;
      } catch {
        dbOk = false;
      }
      return json({
        ok: true,
        service: env.SERVICE_NAME,
        db: dbOk,
        ts: new Date().toISOString(),
      });
    }

    if (url.pathname === "/api/plans" && request.method === "GET") {
      const plans: PlanId[] = ["free", "pro", "business", "agency"];
      return json({
        plans: plans.map((id) => ({ id, features: featuresFor(id) })),
      });
    }

    if (url.pathname === "/api/me" && request.method === "GET") {
      // F1: sessão magic link. F0: stub explícito.
      return json(
        {
          error: "UNAUTHORIZED",
          message: "Magic link auth chega na F1",
        },
        401,
      );
    }

    if (url.pathname === "/" || url.pathname === "/index.html") {
      return new Response(dashboardShell(), {
        headers: { "Content-Type": "text/html; charset=utf-8" },
      });
    }

    return json({ error: "NOT_FOUND" }, 404);
  },
} satisfies ExportedHandler<Env>;

function dashboardShell(): string {
  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>App · link-na-bio</title>
  <style>
    body{font-family:system-ui,sans-serif;margin:0;background:#f8fafc;color:#0f172a}
    main{max-width:640px;margin:3rem auto;padding:1.5rem;background:#fff;border-radius:12px;border:1px solid #e2e8f0}
    code{background:#f1f5f9;padding:.15rem .4rem;border-radius:4px}
    .muted{color:#64748b}
  </style>
</head>
<body>
  <main>
    <h1>Dashboard</h1>
    <p class="muted">F0 — shell do Worker <code>app</code>. Auth, editor e publish entram na F1.</p>
    <ul>
      <li><a href="/health">/health</a></li>
      <li><a href="/api/plans">/api/plans</a></li>
    </ul>
  </main>
</body>
</html>`;
}
