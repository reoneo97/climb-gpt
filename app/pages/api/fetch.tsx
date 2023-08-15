import type { NextApiRequest, NextApiResponse } from 'next'


async function getData() {
  // Get data submitted in request's body.
  const res =fetch('http://localhost:8000/')
    .then((response) => console.log(response))
  // Guard clause checks for first and last name,
  // and returns early if they are not found
  // if (!post.title || !post.description) {
  //   // Sends a HTTP bad request error code
  //   return res.status(400).json({ data: 'First or last name not found' });
  // }
  return res.json()
}
export default async function Page() {
  const data = await getData();
 
  return <main></main>;
}