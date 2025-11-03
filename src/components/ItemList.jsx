import React from 'react';

function ItemList({ items, toggleItem, selectedCategory, searchTerm }) {
  // Filtrar por categoria
  const filteredByCategory = selectedCategory === 'Todas'
    ? items
    : items.filter(item => item.category === selectedCategory);

  // Filtrar por busca
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

  // Estatísticas
  const totalItems = filteredItems.length;
  const checkedItems = filteredItems.filter(item => item.checked).length;

  return (
    <div className="item-list">
      {/* Estatísticas */}
      <div className="stats">
        <span className="stats-text">
          {checkedItems} de {totalItems} {totalItems === 1 ? 'item marcado' : 'itens marcados'}
        </span>
      </div>

      {/* Lista de itens agrupados por categoria */}
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
                  {!item.isFixed && <span className="custom-badge">Novo</span>}
                </label>
              ))}
            </div>
          </div>
        ))
      )}
    </div>
  );
}

export default ItemList;
