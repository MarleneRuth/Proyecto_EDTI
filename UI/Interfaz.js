/**
 * UI/interfaz.js
 * Se encarga de renderizar el tablero y capturar eventos de teclado.
 */

class UI2048 {
    constructor(containerId) {
        this.container = document.getElementById(containerId);
        this.gridSize = 4;
    }

    // Crea la estructura visual inicial
    inicializarDibujo() {
        this.container.innerHTML = '';
        this.container.style.display = 'grid';
        this.container.style.gridTemplateColumns = `repeat(${this.gridSize}, 100px)`;
        this.container.style.gridGap = '10px';
        this.container.style.backgroundColor = '#bbada0';
        this.container.style.padding = '10px';
        this.container.style.borderRadius = '5px';
    }

    // Actualiza el tablero basándose en una matriz de datos
    actualizarTablero(matriz) {
        this.container.innerHTML = ''; // Limpiar previo
        
        matriz.forEach(fila => {
            fila.forEach(valor => {
                const celda = document.createElement('div');
                celda.classList.add('celda');
                
                // Estilo básico de la celda
                celda.style.width = '100px';
                celda.style.height = '100px';
                celda.style.display = 'flex';
                celda.style.alignItems = 'center';
                celda.style.justifyContent = 'center';
                celda.style.fontSize = '24px';
                celda.style.fontWeight = 'bold';
                celda.style.borderRadius = '3px';
                
                // Colores lógicos (puedes expandir esto)
                celda.style.backgroundColor = valor === 0 ? '#cdc1b4' : '#eee4da';
                celda.textContent = valor !== 0 ? valor : '';
                
                this.container.appendChild(celda);
            });
        });
    }

    // Escucha las flechas del teclado
    configurarControles(callbackMovimiento) {
        window.addEventListener('keydown', (e) => {
            const teclas = {
                'ArrowUp': 'W',
                'ArrowDown': 'S',
                'ArrowLeft': 'A',
                'ArrowRight': 'D'
            };
            
            if (teclas[e.key]) {
                callbackMovimiento(teclas[e.key]);
            }
        });
    }
}

// Exportar para usar en otros archivos
export default UI2048;