import { z, defineCollection} from 'astro:content';

const postsCollection = defineCollection({
    type: 'content',
    schema: z.object({
        title: z.string(),
        date: z.string(),
        tags: z.array(z.string()),
        categories: z.array(z.string()),
        emoji: z.string().optional(),
    }),
})

export const collection = {
    'posts': postsCollection,
}