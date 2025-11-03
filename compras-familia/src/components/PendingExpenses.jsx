import React, { useState } from 'react';

function PendingExpenses({ expenses, onApprove, onReject, profile }) {
  const [showForm, setShowForm] = useState(false);
  const [formData, setFormData] = useState({
    description: '',
    amount: '',
    date: new Date().toISOString().split('T')[0],
    receipt: null,
  });

  const pendingExpenses = expenses.filter(exp => exp.status === 'pending');

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.description.trim() || !formData.amount) {
      alert('Por favor, preencha todos os campos');
      return;
    }

    const newExpense = {
      id: `exp-${Date.now()}`,
      ...formData,
      amount: parseFloat(formData.amount),
      status: 'pending',
      createdAt: new Date().toISOString(),
    };

    // Esta função será passada do App.jsx
    if (window.addExpense) {
      window.addExpense(newExpense);
    }

    // Limpar formulário
    setFormData({
      description: '',
      amount: '',
      date: new Date().toISOString().split('T')[0],
      receipt: null,
    });
    setShowForm(false);
  };

  const formatCurrency = (value) => {
    return new Intl.NumberFormat('pt-BR', {
      style: 'currency',
      currency: 'BRL'
    }).format(value);
  };

  const formatDate = (dateString) => {
    return new Date(dateString).toLocaleDateString('pt-BR');
  };

  return (
    <div className="pending-expenses">
      <div className="section-header">
        <h2>💰 Contas Pendentes</h2>
        {profile === 'caregiver' && (
          <button className="btn-add" onClick={() => setShowForm(!showForm)}>
            + Nova Despesa
          </button>
        )}
      </div>

      {/* Formulário de nova despesa (apenas para cuidadora) */}
      {showForm && profile === 'caregiver' && (
        <form className="expense-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Descrição:</label>
            <input
              type="text"
              value={formData.description}
              onChange={(e) => setFormData({ ...formData, description: e.target.value })}
              placeholder="Ex: Compras do mercado"
              className="form-input"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label>Valor (R$):</label>
              <input
                type="number"
                step="0.01"
                value={formData.amount}
                onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
                placeholder="0.00"
                className="form-input"
              />
            </div>

            <div className="form-group">
              <label>Data:</label>
              <input
                type="date"
                value={formData.date}
                onChange={(e) => setFormData({ ...formData, date: e.target.value })}
                className="form-input"
              />
            </div>
          </div>

          <div className="form-actions">
            <button type="button" onClick={() => setShowForm(false)} className="btn-secondary">
              Cancelar
            </button>
            <button type="submit" className="btn-primary">
              Cadastrar
            </button>
          </div>
        </form>
      )}

      {/* Lista de despesas pendentes */}
      <div className="expenses-list">
        {pendingExpenses.length === 0 ? (
          <div className="empty-state">
            <p>Nenhuma conta pendente</p>
          </div>
        ) : (
          pendingExpenses.map((expense) => (
            <div key={expense.id} className="expense-card">
              <div className="expense-info">
                <h3 className="expense-description">{expense.description}</h3>
                <p className="expense-date">{formatDate(expense.date)}</p>
                <p className="expense-amount">{formatCurrency(expense.amount)}</p>
              </div>

              {profile === 'family' && (
                <div className="expense-actions">
                  <button
                    className="btn-approve"
                    onClick={() => onApprove(expense.id)}
                  >
                    ✓ Aprovar
                  </button>
                  <button
                    className="btn-reject"
                    onClick={() => onReject(expense.id)}
                  >
                    ✕ Rejeitar
                  </button>
                </div>
              )}
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default PendingExpenses;
