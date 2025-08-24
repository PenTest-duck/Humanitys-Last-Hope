import { getDays } from "@/api/client";

export default async function VaultPage() {
  const days = await getDays();

  return (
    <div>
      {days.map((day) => (
        <div key={day.date}>
          <h2>{day.date}</h2>
          <p>{day.note}</p>
        </div>
      ))}
    </div>
  );
}
