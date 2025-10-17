const DATA_FILE = 'data.json';

// Função para buscar e renderizar os dados
async function loadData() {
    try {
        const response = await fetch(DATA_FILE);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        
        renderTabela(data.tabela);
        renderArtilharia(data.artilharia);
        document.getElementById('last-update').textContent = `Última atualização: ${data.ultima_atualizacao}`;

    } catch (error) {
        console.error("Erro ao carregar os dados:", error);
        document.getElementById('last-update').textContent = "Erro ao carregar os dados. Tente novamente mais tarde.";
    }
}

// Função para renderizar a Tabela de Classificação
function renderTabela(tabela) {
    const tbody = document.querySelector('#tabela-classificacao tbody');
    tbody.innerHTML = ''; // Limpa o conteúdo anterior

    tabela.forEach(time => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${time.pos}</td>
            <td>${time.time}</td>
            <td><strong>${time.pts}</strong></td>
            <td>${time.jogos}</td>
            <td>${time.e}</td>
            <td>${time.d}</td>
            <td>${time.gp}</td>
            <td>${time.gc}</td>
        `;
    });
}

// Função para renderizar a Tabela de Artilharia
function renderArtilharia(artilharia) {
    const tbody = document.querySelector('#tabela-artilharia tbody');
    tbody.innerHTML = ''; // Limpa o conteúdo anterior

    artilharia.forEach(artilheiro => {
        const row = tbody.insertRow();
        row.innerHTML = `
            <td>${artilheiro.pos}</td>
            <td>${artilheiro.jogador}</td>
            <td>${artilheiro.time}</td>
            <td><strong>${artilheiro.gols}</strong></td>
        `;
    });
}

// Inicia o carregamento dos dados quando a página é carregada
document.addEventListener('DOMContentLoaded', loadData);

