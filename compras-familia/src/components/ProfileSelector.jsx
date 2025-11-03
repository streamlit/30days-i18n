export default function ProfileSelector({ onSelect }) {
  return (
    <div className="flex flex-col items-center justify-center gap-6 h-screen px-6 text-center">
      <h1 className="text-2xl font-semibold text-[#3a4a43]">
        Quem está usando o app?
      </h1>
      <p className="text-[#6b7c74] max-w-md">
        Esse app foi feito pra facilitar a rotina da família e de quem cuida. Escolhe seu perfil:
      </p>
      <div className="flex gap-4 flex-wrap justify-center">
        <button
          onClick={() => onSelect("familia")}
          className="bg-[#73918a] text-white px-6 py-3 rounded-xl shadow-md hover:opacity-90"
        >
          Sou Família
        </button>
        <button
          onClick={() => onSelect("cuidadora")}
          className="bg-white text-[#73918a] border border-[#73918a] px-6 py-3 rounded-xl shadow-md hover:bg-[#f0f3f2]"
        >
          Sou Cuidadora
        </button>
      </div>
      <p className="text-sm text-[#6b7c74] mt-4">
        Feito com carinho para quem cuida 💛
      </p>
    </div>
  );
}
