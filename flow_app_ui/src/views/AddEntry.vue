<script setup>
import { ref } from "vue"
import { useAxios } from "../composables/useAxios.js"
import streets from "../constants/streets.js"

function getNow() {
  const now = new Date()
  return now.toISOString().slice(0,16)
}

const apiItems = useAxios('postage')
const items = ref([])
const newItem = ref({
  track_number: "",
  recipient_street: "",
  recipient_build: "",
  small_package: false,
  delivered_date: getNow()
})

// завантажити всі записи
async function loadItems() {
  items.value = await apiItems.get()
}

// додати новий запис
async function addItem() {
  try {
    const created = await apiItems.add(newItem.value)
    items.value.push(created) // одразу додаємо у список
    newItem.value = { track_number: "", recipient_street: "", delivered_date: "" } // очистити форму
  } catch (err) {
    console.error("Error adding item:", err)
  }
}


loadItems()
</script>

<template>
  <div class="d-flex justify-content-between flex-wrap flex-md-nowrap align-items-center pt-3 pb-2 mb-3 border-bottom">
    <h1 class="h2">Add Entry</h1>
  </div>
  <ul>
    <li v-for="item in items" :key="item.id">
      {{ item.track_number }} — {{ streets[item.recipient_street] }} {{ item.recipient_build }} <span v-if="item.small_package"> — Маленька посилка</span> — {{ item.delivered_date }}
    </li>
  </ul>

  <h3>Add new entry</h3>
  <form @submit.prevent="addItem">
    <input v-model="newItem.track_number" class="form-control" placeholder="Track number" maxlength="13" minlength="13"/>
    <select v-model="newItem.recipient_street" class="form-control">
      <option value="">-- Оберіть вулицю --</option>
      <option value="SHKI">Шкільна</option>
      <option value="GONT">Гонти</option>
      <option value="LUKR">Лесі Українки</option>
      <option value="MAZE">Мазепи</option>
      <option value="BOGU">Богуна</option>
      <option value="HMEL">Б. Хмельницького</option>
      <option value="LISN">Лісна</option>
      <option value="PIDL">Підлісна</option>
      <option value="STUS">Стуса</option>
      <option value="FRAN">І. Франка</option>
      <option value="SAGA">Сагайдачного</option>
      <option value="SHEV">Т. Шевченка</option>
      <option value="BAND">С. Бандери</option>
    </select>
    <label for="small_package">Маленька посилка</label>
    <input type="checkbox" v-model="newItem.small_package" name="small_package">
    <input type="datetime-local" v-model="newItem.delivered_date" class="form-control" />
    <button type="submit" class="btn btn-outline-success">Add</button>
  </form>
</template>

<style scoped>

</style>