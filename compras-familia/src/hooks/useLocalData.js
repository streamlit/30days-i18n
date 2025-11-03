import { useState } from "react";
import { familyMembers, caregivers, expenses, fixedList } from "../data/seedData";

const STORAGE_KEY = "compras-da-familia-data-v1";

export function useLocalData() {
  const getSavedData = () => {
    const saved = localStorage.getItem(STORAGE_KEY);
    return saved ? JSON.parse(saved) : null;
  };

  const initialData = getSavedData() || {
    familyMembers,
    caregivers,
    expenses,
    fixedList
  };

  const [data, setData] = useState(initialData);

  const saveData = (newData) => {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(newData));
    setData(newData);
  };

  return [data, saveData];
}
