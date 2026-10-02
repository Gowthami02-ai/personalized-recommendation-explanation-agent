export const metadata = {
  title: "Recommendation Explanation Agent",
  description: "Retail recommendation explanation and validation demo",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
