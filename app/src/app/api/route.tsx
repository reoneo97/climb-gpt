import { NextResponse } from "next/server";

export async function GET(request: Request) {
  // const { searchParams } = new URL(request.url);
  // const id = searchParams.get("id");
  // const res = await fetch(`http://localhost:8000/`, {
  //   headers: {
  //     "Content-Type": "application/json"
  //   },
  // });
  // const product = await res.json();

  return {'Hello':'World' };
}
