import { describe, expect, it } from "vitest";
import {
  canUseFeature,
  featuresFor,
  isValidSlug,
  linkLimitExceeded,
  parseHost,
  whatsappUrl,
} from "./index.js";

describe("plans", () => {
  it("free shows seal and caps links", () => {
    expect(featuresFor("free").showSeal).toBe(true);
    expect(linkLimitExceeded("free", 8)).toBe(true);
    expect(linkLimitExceeded("free", 7)).toBe(false);
  });

  it("pro unlocks analytics and domain", () => {
    expect(canUseFeature("pro", "analytics")).toBe(true);
    expect(canUseFeature("pro", "customDomain")).toBe(true);
    expect(canUseFeature("free", "analytics")).toBe(false);
  });
});

describe("parseHost", () => {
  const sites = "sites.example.com";

  it("extracts slug from *.sites", () => {
    expect(parseHost("maria.sites.example.com", sites)).toEqual({
      kind: "platform_slug",
      slug: "maria",
    });
  });

  it("treats vanity host as custom", () => {
    expect(parseHost("bio.estudio.com", sites, "example.com")).toEqual({
      kind: "custom",
      hostname: "bio.estudio.com",
    });
  });

  it("rejects www/app of platform zone", () => {
    expect(parseHost("www.example.com", sites, "example.com").kind).toBe(
      "unknown",
    );
  });
});

describe("slug + whatsapp", () => {
  it("validates slug", () => {
    expect(isValidSlug("maria")).toBe(true);
    expect(isValidSlug("www")).toBe(false);
    expect(isValidSlug("-bad")).toBe(false);
  });

  it("builds wa.me url", () => {
    expect(whatsappUrl("+55 11 99999-8888", "Oi")).toBe(
      "https://wa.me/5511999998888?text=Oi",
    );
  });
});
