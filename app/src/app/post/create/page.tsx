export default function Form() {
  return (
    <form action="/api/form" method="post">
      <label htmlFor="title">Title</label>
      <input type="text" id="title" name="title" required />

      <label htmlFor="description">Description</label>
      <input type="text" id="description" name="description" required />

      <label htmlFor="image"></label>
      <input type="file" id="image" name="image"></input>
      <button type="submit">Submit</button>
    </form>
  );
}
