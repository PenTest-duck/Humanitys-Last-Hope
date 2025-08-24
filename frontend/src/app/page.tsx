"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";

export default function Home() {
  const [email, setEmail] = useState("");
  const router = useRouter();

  const handleEnterVault = () => {
    if (email.trim()) {
      router.push("/vault");
    }
  };

  return (
    <div 
      className="min-h-screen flex items-center justify-center p-4 relative"
      style={{
        backgroundImage: 'url("/HLH.png")',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        backgroundRepeat: 'no-repeat'
      }}
    >
      {/* Dark overlay for better text readability */}
      <div className="absolute inset-0 bg-black/50"></div>
      
      {/* Content */}
      <div className="text-center space-y-8 w-full relative z-10">
        {/* Main Title */}
        <h1 className="text-5xl md:text-6xl text-white tracking-tight whitespace-nowrap">
          Humanity's Last Hope
        </h1>
        
        {/* Subtitle */}
        {/* <p className="text-xl md:text-2xl text-gray-300 font-light tracking-wide">
          Become one of humanity's last guardians
        </p> */}
        
        {/* Email Input */}
        <div className="space-y-4 pt-8 w-md mx-auto">
          <Input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="bg-gray-900 border-gray-700 text-white placeholder:text-gray-500 h-12 text-lg"
            onKeyDown={(e) => {
              if (e.key === "Enter" && email.trim()) {
                handleEnterVault();
              }
            }}
          />
          
          {/* Enter Vault Button */}
          <Button
            onClick={handleEnterVault}
            disabled={!email.trim()}
            className="cursor-pointer w-full h-12 text-lg font-semibold bg-gray-500 hover:bg-gray-600 disabled:bg-gray-400 disabled:text-gray-200 disabled:cursor-not-allowed transition-all duration-200"
          >
            Enter the vault
          </Button>
        </div>
      </div>
    </div>
  );
}
