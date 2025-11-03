import React, { useState } from 'react';
import { familyMembers } from '../config/familyConfig';

function FamilySplit({ expenses }) {
  const [startDate, setStartDate] = useState('');
  const [endDate, setEndDate] = useState('');

  const approvedExpenses = expenses.filter(exp => exp.status === 'approved');

  // Filtrar por período
  const filteredExpenses = approvedExpenses.filter(exp => {
    if (!startDate && !endDate) return true;

    const expDate = new Date(exp.date);
    const start = startDate ? new Date(startDate) : null;
    const end = endDate ? new Date(endDate) : null;

    if (start && end) {
      return expDate >= start && expDate <= end;
    } else if (start) {
      return expDate >= start;
    } else if (end) {
      return expDate <= end;
    }
    return true;
  });

  const totalAmount = filteredExpenses.reduce((sum, exp) => sum + exp.amount, 0);

  // Calcular divisão por membro
  const splitByMember = familyMembers.map(member => ({
    ...member,
    amount: totalAmount * member.percent,
  }));

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    }).format(value);
  };

  const formatPercent = (value) => {
    return `${(value * 100).toFixed(0)}%`;
  };

  const clearFilters = () => {
    setStartDate('');
    setEndDate('');
  };

  return (
    <div className="family-split">
      <h2>📊 Divisão Entre Familiares</h2>

      {/* Filtros de período */}
      <div className="filters">
        <div className="filter-group">
          <label>De:</label>
          <input
            type="date"
            value={startDate}
            onChange={(e) => setStartDate(e.target.value)}
            className="form-input"
          />
        </div>

        <div className="filter-group">
          <label>Até:</label>
          <input
            type="date"
            value={endDate}
            onChange={(e) => setEndDate(e.target.value)}
            className="form-input"
          />
        </div>

        <button className="btn-clear-filter" onClick={clearFilters}>
          Limpar
        </button>
      </div>

      {/* Total geral */}
      <div className="total-summary highlight">
        <span>Total de despesas aprovadas:</span>
        <strong>{formatCurrency(totalAmount)}</strong>
      </div>

      {/* Divisão por membro */}
      <div className="split-cards">
        {splitByMember.map((member) => (
          <div
            key={member.id}
            className="split-card"
            style={{ borderLeftColor: member.color }}
          >
            <div className="member-info">
              <h3 className="member-name">{member.name}</h3>
              <span className="member-percent">{formatPercent(member.percent)}</span>
            </div>
            <div className="member-amount">
              {formatCurrency(member.amount)}
            </div>
          </div>
        ))}
      </div>

      {/* Resumo de despesas */}
      <div className="expenses-summary">
        <h3>Despesas do Período ({filteredExpenses.length})</h3>
        {filteredExpenses.length === 0 ? (
          <p className="empty-text">Nenhuma despesa no período selecionado</p>
        ) : (
          <ul className="expenses-summary-list">
            {filteredExpenses.map(exp => (
              <li key={exp.id}>
                <span>{exp.description}</span>
                <span>{formatCurrency(exp.amount)}</span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
}

export default FamilySplit;
