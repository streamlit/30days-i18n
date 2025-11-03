import React, { useState } from 'react';

function ApprovedExpenses({ expenses }) {
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

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    }).format(value);
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('pt-BR');
  };

  const clearFilters = () => {
    setStartDate('');
    setEndDate('');
  };

  return (
    <div className="approved-expenses">
      <h2>✅ Histórico de Contas Aprovadas</h2>

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

      {/* Total do período */}
      <div className="total-summary">
        <span>Total do período:</span>
        <strong>{formatCurrency(totalAmount)}</strong>
      </div>

      {/* Lista de despesas aprovadas */}
      <div className="expenses-list">
        {filteredExpenses.length === 0 ? (
          <div className="empty-state">
            <p>Nenhuma conta aprovada {startDate || endDate ? 'neste período' : ''}</p>
          </div>
        ) : (
          filteredExpenses.map((expense) => (
            <div key={expense.id} className="expense-card approved">
              <div className="expense-info">
                <h3 className="expense-description">{expense.description}</h3>
                <p className="expense-date">{formatDate(expense.date)}</p>
                <p className="expense-amount">{formatCurrency(expense.amount)}</p>
              </div>
              <div className="expense-badge">
                <span className="approved-badge">✓ Aprovada</span>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default ApprovedExpenses;
