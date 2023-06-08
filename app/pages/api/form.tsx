import type { NextApiRequest, NextApiResponse } from 'next'

interface Post{
  title: string
  description: string

}

export default function submitImageHandler(req: NextApiRequest, res: NextApiResponse) {
  // Get data submitted in request's body.
  const post: Post = req.body;
  console.log(post)
  fetch('http://localhost:8000/posts/image',{
      method: 'POST',
      body: post
  })
  .then((response) => console.log(response))
  // Guard clause checks for first and last name,
  // and returns early if they are not found
  // if (!post.title || !post.description) {
  //   // Sends a HTTP bad request error code
  //   return res.status(400).json({ data: 'First or last name not found' });
  // }
  
}