import type { PlanId, SubscriptionStatus } from "./plans.js";

export type { PlanId, SubscriptionStatus };

export type BlockType =
  | "link"
  | "whatsapp"
  | "email"
  | "embed"
  | "highlight"
  | "gallery"
  | "form"
  | "affiliate";

export interface LinkBlock {
  id: string;
  type: "link";
  title: string;
  url: string;
  thumb?: string;
}

export interface WhatsAppBlock {
  id: string;
  type: "whatsapp";
  title: string;
  phone: string;
  message?: string;
}

export interface PageBlock {
  id: string;
  type: BlockType;
  [key: string]: unknown;
}

export interface PageModel {
  kind: "bio" | "institutional" | "portfolio";
  theme: string;
  profile: {
    name: string;
    bio?: string;
    avatarUrl?: string;
  };
  blocks: PageBlock[];
  pages?: Array<{
    slug: string;
    title: string;
    blocks: PageBlock[];
  }>;
  seo?: {
    title?: string;
    description?: string;
    ogImage?: string;
  };
}

export interface PublishJob {
  tenantId: string;
  rev: number;
  requestedAt: string;
}

export type TenantPublicStatus =
  | "draft"
  | "live"
  | "paused_billing"
  | "paused_inactivity";
