import { useState, useEffect } from 'react';
import { INITIAL_ITEMS, CATEGORY_ORDER } from './data/initialItems';
import SearchBar from './components/SearchBar';
import CategoryFilter from './components/CategoryFilter';
import ItemList from './components/ItemList';
import AddItemForm from './components/AddItemForm';
import Footer from './components/Footer';
import './App.css';

const STORAGE_KEY = 'compras-familia-items';

function App() {
  const [items, setItems] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('Todas');
  const [searchTerm, setSearchTerm] = useState('');
  const [showAddForm, setShowAddForm] = useState(false);

  // Carregar dados do localStorage ou usar dados iniciais
  useEffect(() => {
    const savedItems = localStorage.getItem(STORAGE_KEY);

    if (savedItems) {
      try {
        const parsedItems = JSON.parse(savedItems);
        // Mesclar itens salvos com novos itens fixos que possam ter sido adicionados
        const mergedItems = mergeWithInitialItems(parsedItems);
        setItems(mergedItems);
      } catch (error) {
        console.error('Erro ao carregar dados:', error);
        setItems(INITIAL_ITEMS);
      }
    } else {
      setItems(INITIAL_ITEMS);
    }
  }, []);

  // Salvar no localStorage sempre que items mudar
  useEffect(() => {
    if (items.length > 0) {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
    }
  }, [items]);

  // Mesclar itens salvos com itens fixos iniciais
  function mergeWithInitialItems(savedItems) {
    const savedItemsMap = new Map(savedItems.map(item => [item.id, item]));
    const mergedItems = [...savedItems];

    // Adicionar novos itens fixos que não estão nos salvos
    INITIAL_ITEMS.forEach(initialItem => {
      if (!savedItemsMap.has(initialItem.id)) {
        mergedItems.push(initialItem);
      }
    });

    return mergedItems;
  }

  // Alternar estado de marcado/desmarcado
  function toggleItem(id) {
    setItems(prevItems =>
      prevItems.map(item =>
        item.id === id ? { ...item, checked: !item.checked } : item
      )
    );
  }

  // Adicionar novo item
  function addItem({ name, category, isFixed }) {
    const newItem = {
      id: `custom-${Date.now()}`,
      name,
      category,
      isFixed,
      checked: false,
    };

    setItems(prevItems => [...prevItems, newItem]);
  }

  // Obter lista de categorias únicas
  function getCategories() {
    const categoriesSet = new Set(items.map(item => item.category));
    const categories = Array.from(categoriesSet);

    // Ordenar categorias de acordo com CATEGORY_ORDER
    return categories.sort((a, b) => {
      const indexA = CATEGORY_ORDER.indexOf(a);
      const indexB = CATEGORY_ORDER.indexOf(b);

      // Se ambos estão na ordem predefinida, usar essa ordem
      if (indexA !== -1 && indexB !== -1) {
        return indexA - indexB;
      }
      // Se só A está na ordem predefinida, A vem primeiro
      if (indexA !== -1) return -1;
      // Se só B está na ordem predefinida, B vem primeiro
      if (indexB !== -1) return 1;
      // Se nenhum está, ordem alfabética
      return a.localeCompare(b);
    });
  }

  // Limpar itens marcados (apenas itens não-fixos)
  function clearCheckedItems() {
    const confirmed = window.confirm(
      'Deseja limpar todos os itens marcados? (Itens fixos serão apenas desmarcados)'
    );

    if (confirmed) {
      setItems(prevItems =>
        prevItems
          .filter(item => !item.checked || item.isFixed) // Manter fixos
          .map(item => ({ ...item, checked: false })) // Desmarcar todos
      );
    }
  }

  const categories = getCategories();

  return (
    <div className="app">
      <header className="header">
        <h1 className="app-title">🛒 Compras da Família</h1>
        <p className="app-subtitle">Lista da Dona Judith</p>
      </header>

      <main className="main-content">
        <SearchBar searchTerm={searchTerm} setSearchTerm={setSearchTerm} />

        <CategoryFilter
          categories={categories}
          selectedCategory={selectedCategory}
          setSelectedCategory={setSelectedCategory}
        />

        <div className="actions-bar">
          <button
            className="btn-add"
            onClick={() => setShowAddForm(true)}
          >
            + Adicionar Item
          </button>

          <button
            className="btn-clear"
            onClick={clearCheckedItems}
          >
            Limpar Marcados
          </button>
        </div>

        <ItemList
          items={items}
          toggleItem={toggleItem}
          selectedCategory={selectedCategory}
          searchTerm={searchTerm}
        />
      </main>

      {showAddForm && (
        <AddItemForm
          categories={categories}
          addItem={addItem}
          onClose={() => setShowAddForm(false)}
        />
      )}

      <Footer />
    </div>
  );
}

export default App;
