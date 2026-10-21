/** Generated from data/motion-prompts.json. Run python3 scripts/build.py. */
export const MOTION_CATEGORIES = ["Product UI", "Phone", "Charts", "Diagrams", "Kinetic type", "Shapes", "Particles", "Characters", "Photos", "Music", "Code"] as const;
export type MotionCategory = (typeof MOTION_CATEGORIES)[number];
export type MotionEntry = {
  id: string; title: string; author: string; type: 'Prompt' | 'Skill'; model: string;
  categories: MotionCategory[]; prompt: string; sourceUrl: string; promptSourceUrl: string;
  collectionUrl: string; poster: string; video?: string; width: number; height: number; skillUrl?: string; requiresReference?: boolean;
};
export const MOTION_ENTRIES: MotionEntry[] = [];
export const MOTION_RESOURCES = [];
