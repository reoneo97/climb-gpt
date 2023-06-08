import type { NextApiRequest, NextApiResponse } from "next";

// function getData() {
//   // Get data submitted in request's body.
//   const res = fetch("http://localhost:8000/", {
//     method: 'GET',
//     headers: {
//       "Access-Control-Allow-Origin": "*",
//       "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
//       "Access-Control-Allow-Headers": "Content-Type, Authorization",
//     },
//   })
//     .then((response) => console.log(response))

// }
export default function Page() {
  const data = getData();
  console.log(data);

  return 
    <div>
    </div>;
}
