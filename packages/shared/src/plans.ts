/** Planos comerciais — fonte única de gates (UC-72 / UC-95). */
export type PlanId = "free" | "pro" | "business" | "agency";

export type SubscriptionStatus =
  | "active"
  | "trialing"
  | "past_due"
  | "paused"
  | "canceled";

export interface PlanFeatures {
  maxLinks: number | null;
  showSeal: boolean;
  customDomain: boolean;
  analytics: boolean;
  exportZip: boolean;
  embeds: boolean;
  gallery: boolean;
  highlights: boolean;
  qrCode: boolean;
  multiPage: boolean;
  formLeads: boolean;
  maxSites: number;
  premiumSkins: boolean;
}

export const PLAN_FEATURES: Record<PlanId, PlanFeatures> = {
  free: {
    maxLinks: 8,
    showSeal: true,
    customDomain: false,
    analytics: false,
    exportZip: false,
    embeds: false,
    gallery: false,
    highlights: false,
    qrCode: false,
    multiPage: false,
    formLeads: false,
    maxSites: 1,
    premiumSkins: false,
  },
  pro: {
    maxLinks: null,
    showSeal: false,
    customDomain: true,
    analytics: true,
    exportZip: true,
    embeds: true,
    gallery: true,
    highlights: true,
    qrCode: true,
    multiPage: false,
    formLeads: false,
    maxSites: 1,
    premiumSkins: true,
  },
  business: {
    maxLinks: null,
    showSeal: false,
    customDomain: true,
    analytics: true,
    exportZip: true,
    embeds: true,
    gallery: true,
    highlights: true,
    qrCode: true,
    multiPage: true,
    formLeads: true,
    maxSites: 2,
    premiumSkins: true,
  },
  agency: {
    maxLinks: null,
    showSeal: false,
    customDomain: true,
    analytics: true,
    exportZip: true,
    embeds: true,
    gallery: true,
    highlights: true,
    qrCode: true,
    multiPage: true,
    formLeads: true,
    maxSites: 25,
    premiumSkins: true,
  },
};

export function featuresFor(plan: PlanId): PlanFeatures {
  return PLAN_FEATURES[plan];
}

export function canUseFeature(
  plan: PlanId,
  feature: keyof PlanFeatures,
): boolean {
  const value = PLAN_FEATURES[plan][feature];
  if (typeof value === "boolean") return value;
  if (typeof value === "number") return value > 0;
  return value === null; // null maxLinks = unlimited
}

export function linkLimitExceeded(plan: PlanId, currentLinks: number): boolean {
  const max = PLAN_FEATURES[plan].maxLinks;
  if (max === null) return false;
  return currentLinks >= max;
}
