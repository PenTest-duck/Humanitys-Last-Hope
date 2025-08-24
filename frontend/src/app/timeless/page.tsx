"use client";

export default function TimelessPage() {
  return (
    <div 
      className="min-h-screen flex items-center justify-center p-8 relative"
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
      <div className="text-center space-y-8 w-full max-w-4xl relative z-10">
        
        {/* Timeless Text Content */}
        <div className="bg-black/30 backdrop-blur-sm rounded-lg p-8">
          <p className="text-lg md:text-xl text-gray-200 leading-relaxed text-left">
            Across all cultures, civilizations, and epochs, humanity has consistently gravitated toward a constellation of fundamental values that transcend time, geography, and circumstance: the sacred worth and dignity of every human life; compassion that extends beyond tribe and kin to embrace all beings capable of suffering; the pursuit of truth through reason, observation, and wisdom; justice that seeks fairness and protects the vulnerable from the powerful; freedom of thought, expression, and self-determination balanced with responsibility to the common good; love that binds us in relationships of care, sacrifice, and mutual flourishing; beauty that elevates the spirit and connects us to something greater than ourselves; courage to act rightly in the face of fear and adversity; humility that recognizes our limitations and interconnectedness; and hope that persists through darkness and drives us toward a better future. These values emerge not from any single tradition but from the deepest wells of human experience—they are written in our capacity for moral reasoning, encoded in our literature and philosophy, and demonstrated by every act of selfless love, every stand against injustice, every search for understanding that has ever moved the human heart toward what is noble and true.
          </p>
        </div>
      </div>
    </div>
  );
}
