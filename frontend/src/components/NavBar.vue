<template>
  <div class="sidebar">
    <h1 class="logo">RAICHUU</h1>
    <ul class="nav-links">
      <RouterLink to="/"> <li class="sidebar-item">Home</li></RouterLink>
      <!-- <RouterLink to=""><li class="sidebar-item">Hello</li></RouterLink> -->
    </ul>
  </div>
</template>
<script>
export default {}
</script>
<style>
@import '/src/assets/base.css';

.sidebar {
  height: 100vh;
  width: 250px;
  /* border-right: 1px solid rgba(40, 40, 40, 0.2); */
  background-color: var(--primary-color);
  box-shadow: 0.5px 0px 10px rgba(40, 40, 40, 0.1);
  padding: 1.25rem 1.85rem;
}

.nav-links {
  position: relative;
  padding: 0;
}

li {
  /* margin-left: -100px; */
  text-decoration: none;
  text-align: center;
  list-style: none;
  font-size: var(--h3-font-size);
  padding: 0.625rem 0;
  color: var(--vt-c-white-soft);
  font-weight: var(--font-bold);
}

h1 {
  font-weight: var(--font-bold);
  font-size: var(--h1-font-size);
  color: var(--primary-color);
}

.logo {
  text-align: center;
  color: var(--vt-c-white-soft);
  margin-bottom: 8rem;
}

.btn1 {
  margin: 0.5rem 0 0 0;
  width: 100px;
  height: 40px;
  background-color: var(--primary-color);
  border: none;
  color: var(--vt-c-white-soft);
}

li:hover {
  background-color: white;
  color: var(--primary-color);
}
</style>
