export const familyMembers = [
  { id: "m1", name: "João", percent: 0.5 },
  { id: "m2", name: "Maria", percent: 0.3 },
  { id: "m3", name: "Lúcia", percent: 0.2 }
];

export const caregivers = [
  { id: "c1", name: "Ana", role: "Cuidadora Principal" },
  { id: "c2", name: "Beatriz", role: "Cuidadora Auxiliar" }
];

export const expenses = [
  {
    id: "exp1",
    descricao: "Compras da semana",
    valor: 280.0,
    status: "pendente",
    quemLancou: "c1",
    data: "2025-10-28",
    itens: ["Arroz", "Feijão", "Leite", "Tomate", "Pão"],
    observacao: "Compras da Dona Judith - feira da semana",
    divisao: []
  },
  {
    id: "exp2",
    descricao: "Medicamentos de rotina",
    valor: 150.0,
    status: "aprovado",
    quemLancou: "c2",
    data: "2025-10-20",
    itens: ["Paracetamol", "Vitamina D"],
    observacao: "Compras na farmácia São João",
    divisao: [
      { memberId: "m1", valor: 75 },
      { memberId: "m2", valor: 45 },
      { memberId: "m3", valor: 30 }
    ]
  }
];

export const fixedList = {
  title: "Lista Fixa Dona Judith",
  categorias: {
    "Verduras e Legumes": [
      "Alface",
      "Rúcula",
      "Agrião",
      "Escarola",
      "Couve",
      "Cheiro Verde",
      "Coentro",
      "Couve flor",
      "Brócolis",
      "Espinafre"
    ],
    "Temperos e Hortaliças": [
      "Alho",
      "Cebola",
      "Tomate",
      "Batata",
      "Cenoura",
      "Abobrinha",
      "Abóbora",
      "Inhame",
      "Gengibre",
      "Beterraba",
      "Mandioquinha"
    ],
    "Frutas": [
      "Laranja",
      "Limão",
      "Mamão",
      "Manga",
      "Abacaxi",
      "Banana",
      "Maçã",
      "Pera"
    ],
    "Laticínios": [
      "Manteiga",
      "Requeijão",
      "Iogurte",
      "Queijo Mussarela",
      "Yakult"
    ],
    "Pães e Biscoitos": [
      "Pão de forma",
      "Bisnaguinha",
      "Bolacha de Sal",
      "Bolacha de Maisena"
    ],
    "Bebidas e Matinais": [
      "Leite Integral",
      "Chás (camomila , cidreira)",
      "Suco de Uva",
      "Café",
      "Açúcar Branco",
      "Açúcar Orgânico",
      "Gelatina",
      "Geléia"
    ],
    "Mercearia": [
      "Arroz Branco",
      "Arroz Integral",
      "Feijão",
      "Lentilha",
      "Óleo de Milho",
      "Sal",
      "Macarrão",
      "Macarrão para sopa",
      "Molho de Tomate",
      "Leite Condensado",
      "Caldo de Carne",
      "Colorífico Kitano",
      "Farinha de trigo",
      "Ovos",
      "Misturas",
      "Azeite",
      "Vinagre"
    ],
    "Higiene e Limpeza": [
      "Detergente",
      "Sabonete",
      "Creme dental",
      "Lenço Umedecido",
      "Leite de Colônia",
      "Creme Nívea (latinha)",
      "Hidratante (corporal)",
      "Repelente",
      "Sabonete líquido"
    ],
    "Itens de Casa": [
      "Papel Higiênico",
      "Guardanapo",
      "Fósforos",
      "Bombril",
      "Desinfetante",
      "Cândida",
      "Buchinha de louça"
    ]
  }
};
