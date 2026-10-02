"use client";

import { useState } from "react";

export default function HomePage() {
  const [input, setInput] = useState("");

  return (
    <main style={{ padding: 32, maxWidth: 1200, margin: "0 auto", fontFamily: "sans-serif" }}>
      <h1>Personalized Recommendation Explanation Agent</h1>
      <p>Grounded recommendations explained with verified attributes and customer constraints.</p>

      <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(260px, 1fr))", gap: 20, marginTop: 24 }}>
        <section style={{ border: "1px solid #ddd", borderRadius: 12, padding: 20, background: "#fff" }}>
          <h2>Conversation</h2>
          <div style={{ marginBottom: 12, minHeight: 120, border: "1px solid #eee", borderRadius: 8, padding: 12 }}>
            <p><strong>User:</strong> Why is this product recommended for me?</p>
            <p><strong>Agent:</strong> It matches your budget and style preferences, and it is in stock.</p>
          </div>
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about a recommendation..."
            style={{ width: "100%", padding: 10, borderRadius: 8, border: "1px solid #ccc" }}
          />
        </section>

        <section style={{ border: "1px solid #ddd", borderRadius: 12, padding: 20, background: "#fff" }}>
          <h2>Workflow Panel</h2>
          <ul>
            <li>Triage</li>
            <li>Retrieval</li>
            <li>Investigation</li>
            <li>Validation</li>
            <li>Response</li>
          </ul>
        </section>

        <section style={{ border: "1px solid #ddd", borderRadius: 12, padding: 20, background: "#fff" }}>
          <h2>Sources</h2>
          <ul>
            <li>Product catalog</li>
            <li>Customer constraints</li>
            <li>Recommendation policy</li>
          </ul>
        </section>
      </div>
    </main>
  );
}
