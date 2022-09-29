# WebServer

Tarefa desenvolvida na disciplina de redes pelo professor Marcos Courino no curso Análise e desenvolvimento de Sistemas no IFRS.

Nesta tarefa, foi desenvolvido um servidor Web simples em Python, capaz de processar apenas uma requisicao. O servidor Web cria um socket de conexão quando contatado por um cliente (navegador); 
Recebe a requisição HTTP dessa conexão; Analisa a requisição para determinar o arquivo específico sendo requisitado;
Obtém o arquivo requisitado do sistema de arquivo do servidor; 
Cria uma mensagem de resposta HTTP consistindo no arquivo requisitado precedido por linhas de cabeçalho;
Envia a resposta pela conexão TCP ao navegador requisitante. 
Se um navegador requisitar um arquivo que não está presente no servidor, o servidor retorna uma mensagem de erro “404 Not Found”.
