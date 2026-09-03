/**
 * Parse Host → slug ou hostname custom.
 * Path-based tenant é proibido quando há CNAME (docs/tenants-e-dominios.md).
 */

export type HostLookup =
  | { kind: "platform_slug"; slug: string }
  | { kind: "custom"; hostname: string }
  | { kind: "unknown" };

const RESERVED_SLUGS = new Set([
  "www",
  "app",
  "sites",
  "api",
  "mail",
  "cdn",
  "static",
  "admin",
  "status",
  "help",
  "docs",
]);

export function isReservedSlug(slug: string): boolean {
  return RESERVED_SLUGS.has(slug.toLowerCase());
}

export function isValidSlug(slug: string): boolean {
  if (!/^[a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?$/.test(slug)) return false;
  if (isReservedSlug(slug)) return false;
  return true;
}

/**
 * @param host Header Host sem porta
 * @param sitesZone Ex.: "sites.linkk.ae"
 * @param platformZone Ex.: "linkk.ae" — hosts www/app caem em unknown aqui
 */
export function parseHost(
  host: string,
  sitesZone: string,
  platformZone?: string,
): HostLookup {
  const hostname = host.toLowerCase().split(":")[0] ?? "";
  if (!hostname) return { kind: "unknown" };

  const suffix = `.${sitesZone.toLowerCase()}`;
  if (hostname === sitesZone.toLowerCase()) {
    return { kind: "unknown" };
  }
  if (hostname.endsWith(suffix)) {
    const slug = hostname.slice(0, -suffix.length);
    if (!slug || slug.includes(".")) return { kind: "unknown" };
    return { kind: "platform_slug", slug };
  }

  if (platformZone) {
    const zone = platformZone.toLowerCase();
    if (hostname === zone || hostname === `www.${zone}` || hostname === `app.${zone}`) {
      return { kind: "unknown" };
    }
  }

  // Qualquer outro host = potencial custom domain
  if (hostname.includes(".")) {
    return { kind: "custom", hostname };
  }

  return { kind: "unknown" };
}

export function whatsappUrl(phone: string, message?: string): string {
  const digits = phone.replace(/\D/g, "");
  const base = `https://wa.me/${digits}`;
  if (!message) return base;
  return `${base}?text=${encodeURIComponent(message)}`;
}
