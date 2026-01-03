const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.json());

// Ruta raíz
app.get('/', (req, res) => {
  res.send('🛰️ Orión está activo y escuchando...');
});

// Ruta para comandos JSON
app.post('/comando', (req, res) => {
  const comando = req.body;
  console.log('📥 Comando recibido:', comando);
  res.json({ estado: 'ok', recibido: comando });
});

// Ruta de estado
app.get('/estado', (req, res) => {
  res.json({ estado: 'activo', hora: new Date().toISOString() });
});

app.listen(PORT, () => {
  console.log(`🚀 Servidor Orión corriendo en puerto ${PORT}`);
});
