import React, { useState, useEffect } from 'react';
import { FIXED_ITEMS, CATEGORY_ORDER } from '../data/fixedList';

function FixedList() {
  const [items, setItems] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('Todas');

  // Carregar do localStorage ou usar dados iniciais
  useEffect(() => {
    const saved = localStorage.getItem('fixed-list-items');
    if (saved) {
      try {
        setItems(JSON.parse(saved));
      } catch (error) {
        console.error('Erro ao carregar lista:', error);
        setItems(FIXED_ITEMS);
      }
    } else {
      setItems(FIXED_ITEMS);
    }
  }, []);

  // Salvar no localStorage
  useEffect(() => {
    if (items.length > 0) {
      localStorage.setItem('fixed-list-items', JSON.stringify(items));
    }
  }, [items]);

  const toggleItem = (id) => {
    setItems(prevItems =>
      prevItems.map(item =>
        item.id === id ? { ...item, checked: !item.checked } : item
      )
    );
  };

  const clearChecked = () => {
    if (window.confirm('Desmarcar todos os itens?')) {
      setItems(prevItems =>
        prevItems.map(item => ({ ...item, checked: false }))
      );
    }
  };

  // Filtrar por categoria e busca
  const filteredByCategory = selectedCategory === 'Todas'
    ? items
    : items.filter(item => item.category === selectedCategory);

  const filteredItems = searchTerm
    ? filteredByCategory.filter(item =>
        item.name.toLowerCase().includes(searchTerm.toLowerCase())
      )
    : filteredByCategory;

  // Agrupar por categoria
  const groupedItems = filteredItems.reduce((acc, item) => {
    if (!acc[item.category]) {
      acc[item.category] = [];
    }
    acc[item.category].push(item);
    return acc;
  }, {});

  const categories = Array.from(new Set(items.map(item => item.category))).sort((a, b) => {
    const indexA = CATEGORY_ORDER.indexOf(a);
    const indexB = CATEGORY_ORDER.indexOf(b);
    if (indexA !== -1 && indexB !== -1) return indexA - indexB;
    if (indexA !== -1) return -1;
    if (indexB !== -1) return 1;
    return a.localeCompare(b);
  });

  const totalItems = filteredItems.length;
  const checkedItems = filteredItems.filter(item => item.checked).length;

  return (
    <div className="fixed-list">
      <h2>📝 Lista Fixa da Dona Judith</h2>

      {/* Barra de busca */}
      <div className="search-bar">
        <input
          type="text"
          placeholder="🔍 Buscar produto..."
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
          className="search-input"
        />
      </div>

      {/* Filtro de categorias */}
      <div className="category-filter">
        <button
          className={`category-btn ${selectedCategory === 'Todas' ? 'active' : ''}`}
          onClick={() => setSelectedCategory('Todas')}
        >
          Todas
        </button>
        {categories.map((category) => (
          <button
            key={category}
            className={`category-btn ${selectedCategory === category ? 'active' : ''}`}
            onClick={() => setSelectedCategory(category)}
          >
            {category}
          </button>
        ))}
      </div>

      {/* Estatísticas */}
      <div className="stats">
        <span className="stats-text">
          {checkedItems} de {totalItems} {totalItems === 1 ? 'item marcado' : 'itens marcados'}
        </span>
        <button className="btn-clear-checked" onClick={clearChecked}>
          Limpar Marcações
        </button>
      </div>

      {/* Lista de itens */}
      <div className="items-container">
        {Object.keys(groupedItems).length === 0 ? (
          <div className="empty-state">
            <p>Nenhum item encontrado</p>
          </div>
        ) : (
          Object.entries(groupedItems).map(([category, categoryItems]) => (
            <div key={category} className="category-section">
              <h3 className="category-title">{category}</h3>
              <div className="items-grid">
                {categoryItems.map((item) => (
                  <label key={item.id} className={`item-card ${item.checked ? 'checked' : ''}`}>
                    <input
                      type="checkbox"
                      checked={item.checked}
                      onChange={() => toggleItem(item.id)}
                    />
                    <span className="item-name">{item.name}</span>
                  </label>
                ))}
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default FixedList;
