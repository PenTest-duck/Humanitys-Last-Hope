import type { Metadata } from "next";
import { Eczar } from "next/font/google";
import "./globals.css";

const eczar = Eczar({
  variable: "--font-eczar",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Humanity's Last Hope",
  description: "Become one of humanity's last guardians",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={`dark ${eczar.variable}`}>
      <body className="antialiased">
        {children}
      </body>
    </html>
  );
}
