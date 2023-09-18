import Image from "next/image";
import styles from "./page.module.css";
import Link from "next/link";

export default function Home() {
  return (
    <main className={styles.main}>
      <h1>Climb GPT</h1>``
      <div className={styles.grid}>
        <div className={styles.description}>
          <h2>What is this app?</h2>
          <p>
            Use this application to submit your favourite rock climbing routes
            and get advice on your climbing straight away!
          </p>
          <Link href="/post">Create a new post!</Link>
        </div>
      </div>
    </main>
  );
}
