import React, { useState } from 'react';
import PendingExpenses from '../components/PendingExpenses';
import ApprovedExpenses from '../components/ApprovedExpenses';
import FamilySplit from '../components/FamilySplit';
import FixedList from '../components/FixedList';
import { PROFILES } from '../config/familyConfig';

function Dashboard({ profile, expenses, onApprove, onReject, onLogout }) {
  const [activeTab, setActiveTab] = useState('pending');

  const pendingCount = expenses.filter(exp => exp.status === 'pending').length;
  const approvedCount = expenses.filter(exp => exp.status === 'approved').length;

  return (
    <div className="dashboard">
      {/* Header */}
      <header className="dashboard-header">
        <div className="header-content">
          <div className="header-left">
            <h1 className="dashboard-title">🛒 Compras da Família</h1>
            <span className="profile-badge">
              {profile === PROFILES.FAMILY ? '👨‍👩‍👧‍👦 Família' : '💼 Cuidadora'}
            </span>
          </div>
          <button className="btn-logout" onClick={onLogout}>
            ← Trocar Perfil
          </button>
        </div>
      </header>

      {/* Tabs de navegação */}
      <div className="tabs">
        <button
          className={`tab ${activeTab === 'pending' ? 'active' : ''}`}
          onClick={() => setActiveTab('pending')}
        >
          💰 Pendentes
          {pendingCount > 0 && <span className="badge">{pendingCount}</span>}
        </button>

        {profile === PROFILES.FAMILY && (
          <>
            <button
              className={`tab ${activeTab === 'approved' ? 'active' : ''}`}
              onClick={() => setActiveTab('approved')}
            >
              ✅ Histórico
              {approvedCount > 0 && <span className="badge-light">{approvedCount}</span>}
            </button>

            <button
              className={`tab ${activeTab === 'split' ? 'active' : ''}`}
              onClick={() => setActiveTab('split')}
            >
              📊 Divisão
            </button>
          </>
        )}

        <button
          className={`tab ${activeTab === 'list' ? 'active' : ''}`}
          onClick={() => setActiveTab('list')}
        >
          📝 Lista Fixa
        </button>
      </div>

      {/* Conteúdo das tabs */}
      <div className="tab-content">
        {activeTab === 'pending' && (
          <PendingExpenses
            expenses={expenses}
            onApprove={onApprove}
            onReject={onReject}
            profile={profile}
          />
        )}

        {activeTab === 'approved' && profile === PROFILES.FAMILY && (
          <ApprovedExpenses expenses={expenses} />
        )}

        {activeTab === 'split' && profile === PROFILES.FAMILY && (
          <FamilySplit expenses={expenses} />
        )}

        {activeTab === 'list' && (
          <FixedList />
        )}
      </div>

      {/* Footer */}
      <footer className="dashboard-footer">
        <p>Feito com carinho para quem cuida 💛</p>
      </footer>
    </div>
  );
}

export default Dashboard;
