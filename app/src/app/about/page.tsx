import axios from "axios";


async function getData() {
  // Get data submitted in request's body.
  // const res = axios({
  //   method: "get",
  //   url: "http://127.0.0.1:8000/"
  // }).then((response) => console.log(response.data));

  const res = fetch('http://127.0.0.1:8000/')
  return res;
}
export default async function About() {
  const data = await getData();
  const data2 = await data.json()
  console.log(data2)
  return <div>About Jinbesan & Kokjuira</div>;
}
