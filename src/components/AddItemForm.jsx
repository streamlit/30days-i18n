import React, { useState } from 'react';

function AddItemForm({ categories, addItem, onClose }) {
  const [itemName, setItemName] = useState('');
  const [selectedCategory, setSelectedCategory] = useState(categories[0] || '');
  const [newCategory, setNewCategory] = useState('');
  const [isCreatingCategory, setIsCreatingCategory] = useState(false);
  const [isFixed, setIsFixed] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!itemName.trim()) {
      alert('Por favor, digite o nome do produto');
      return;
    }

    const categoryToUse = isCreatingCategory && newCategory.trim()
      ? newCategory.trim()
      : selectedCategory;

    if (!categoryToUse) {
      alert('Por favor, selecione ou crie uma categoria');
      return;
    }

    addItem({
      name: itemName.trim(),
      category: categoryToUse,
      isFixed: isFixed,
    });

    // Limpar formulário
    setItemName('');
    setNewCategory('');
    setIsCreatingCategory(false);
    setIsFixed(false);
    onClose();
  };

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <div className="modal-header">
          <h2>Adicionar Item</h2>
          <button className="close-btn" onClick={onClose}>✕</button>
        </div>

        <form onSubmit={handleSubmit} className="add-item-form">
          <div className="form-group">
            <label>Nome do produto:</label>
            <input
              type="text"
              value={itemName}
              onChange={(e) => setItemName(e.target.value)}
              placeholder="Ex: Leite desnatado"
              className="form-input"
              autoFocus
            />
          </div>

          <div className="form-group">
            <label>Categoria:</label>

            {!isCreatingCategory ? (
              <>
                <select
                  value={selectedCategory}
                  onChange={(e) => setSelectedCategory(e.target.value)}
                  className="form-select"
                >
                  {categories.map((cat) => (
                    <option key={cat} value={cat}>{cat}</option>
                  ))}
                </select>
                <button
                  type="button"
                  onClick={() => setIsCreatingCategory(true)}
                  className="link-btn"
                >
                  + Criar nova categoria
                </button>
              </>
            ) : (
              <>
                <input
                  type="text"
                  value={newCategory}
                  onChange={(e) => setNewCategory(e.target.value)}
                  placeholder="Ex: 🧁 Guloseimas"
                  className="form-input"
                />
                <button
                  type="button"
                  onClick={() => {
                    setIsCreatingCategory(false);
                    setNewCategory('');
                  }}
                  className="link-btn"
                >
                  Usar categoria existente
                </button>
              </>
            )}
          </div>

          <div className="form-group">
            <label className="checkbox-label">
              <input
                type="checkbox"
                checked={isFixed}
                onChange={(e) => setIsFixed(e.target.checked)}
              />
              <span>Colocar na lista fixa da Dona Judith</span>
            </label>
            <small className="help-text">
              Itens fixos sempre aparecem na lista, mesmo quando marcados
            </small>
          </div>

          <div className="form-actions">
            <button type="button" onClick={onClose} className="btn-secondary">
              Cancelar
            </button>
            <button type="submit" className="btn-primary">
              Adicionar
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default AddItemForm;
