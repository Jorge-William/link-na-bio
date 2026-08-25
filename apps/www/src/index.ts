export interface Env {
  ASSETS: Fetcher;
  SERVICE_NAME: string;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);

    if (url.pathname === "/health") {
      return Response.json({
        ok: true,
        service: env.SERVICE_NAME ?? "www",
        ts: new Date().toISOString(),
      });
    }

    return env.ASSETS.fetch(request);
  },
} satisfies ExportedHandler<Env>;
