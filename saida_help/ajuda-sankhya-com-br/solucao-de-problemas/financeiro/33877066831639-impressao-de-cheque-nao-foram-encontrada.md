---
id: "33877066831639"
titulo: "Impressão de Cheque: Não foram encontradas impressoras!"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/33877066831639-Impress%C3%A3o-de-Cheque-N%C3%A3o-foram-encontradas-impressoras"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-07-22T14:28:10Z"
rotulos: ["Configuração", "Impressão", "USAAPPIMPRESSAO", "SPS", "Sankhya Print Service", "Preferências", "Financeiro", "Cheque", "USASERVIMP", "erro", "Não foram encontradas impressoras!", "Impressão de Cheque"]
---

# Impressão de Cheque: Não foram encontradas impressoras!

**MENSAGEM:**

Não foram encontradas impressoras!

**SITUAÇÃO:**

Ao tentar imprimir cheques pela tela **"Impressão de Cheque"** (Financeiro > Relatórios) o sistema não localiza impressoras disponíveis apresentando a mensagem de erro.

**Importante:** Antes de iniciar a solução, verifique se a empresa utiliza o **SPS** (Sankhya Print Service).

Para mais informações, consulte o artigo [Sankhya Print Service](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service).

**SOLUÇÃO:**

**(1)** Na tela **''Preferências''** (Configurações» Avançado» Preferências) desabilite o parâmetro **"USASERVIMP'',** caso o SPS não seja utilizado; 

**(2)** Desabilite o parâmetro **"USAAPPIMPRESSAO"** para garantir que o sistema utilize o plugin de impressão via WebConnection integrado, evitando conflito com aplicações externas; 

**(3)** Se o SPS for utilizado e o parâmetro USASERVIMP estiver ativado, configure apenas um dos métodos de impressão do SPS, conforme o Sankhya Print Service:

- [Configurando por Parâmetros](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporparmetros)
- [Configurando por Nome de Impressora](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandopornomedeimpressora)
- [Configurando por Impressoras e Servidor de impressão](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597714-Sankhya-Print-Service#configurandoporimpressoraseservidordeimpresso)

Configure apenas um método para evitar conflitos. Recomenda-se utilizar **"Impressoras e Servidores de Impressão"**.

**(4)** Mesmo utilizando o SPS, mantenha o parâmetro USAAPPIMPRESSAO desabilitado, conforme orientado no **passo 2**.

**CAUSA:**

A mensagem de erro pode ser exibida por diferentes motivos, geralmente relacionados à configuração do sistema para tratamento de impressão. Os mais comuns são:

- **Incompatibilidade entre os parâmetros de impressão**, especialmente quando o SPS não está em uso, mas o parâmetro USASERVIMP permanece ativado;
- **Parâmetro USAAPPIMPRESSAO ativado**, fazendo com que o sistema aguarde uma aplicação externa de impressão, gerando conflito se não estiver corretamente configurada;
- **Conflito na configuração simultânea dos três métodos de impressão do SPS**, ocultando as impressoras disponíveis mesmo que individualmente estejam corretas.
