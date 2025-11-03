// Configuração dos membros da família e divisão de custos
// EDITE AQUI para mudar os nomes e percentuais

export const familyMembers = [
  {
    id: 'm1',
    name: 'João',
    percent: 0.5,  // 50%
    color: '#6f8f87'
  },
  {
    id: 'm2',
    name: 'Maria',
    percent: 0.3,  // 30%
    color: '#c17c5c'
  },
  {
    id: 'm3',
    name: 'Lúcia',
    percent: 0.2,  // 20%
    color: '#f4d4a8'
  },
];

// Validação: a soma deve ser 100% (1.0)
const totalPercent = familyMembers.reduce((sum, member) => sum + member.percent, 0);
if (Math.abs(totalPercent - 1.0) > 0.001) {
  console.warn(`⚠️ Atenção: A soma dos percentuais é ${(totalPercent * 100).toFixed(1)}%, deveria ser 100%`);
}

// Perfis de acesso
export const PROFILES = {
  FAMILY: 'family',     // Família - aprova contas
  CAREGIVER: 'caregiver' // Cuidadora - cadastra contas
};
