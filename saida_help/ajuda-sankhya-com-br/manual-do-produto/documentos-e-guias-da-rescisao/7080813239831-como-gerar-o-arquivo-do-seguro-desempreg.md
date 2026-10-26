---
id: "7080813239831"
titulo: "Como gerar o arquivo do Seguro-Desemprego"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7080813239831-Como-gerar-o-arquivo-do-Seguro-Desemprego"
trilha: "Manual do Produto > Pessoas+ > Rescisão > Documentos e Guias da Rescisão"
atualizado_em: "2026-10-02T15:46:00Z"
rotulos: ["ID: br.com.sankhya.rh.GerenciadorFolha", "eSocial", "Folha de Pagamento", "Como gerar o arquivo do Seguro Desemprego", "Gerenciador de folhas", "GRRF", "Gere arquivo seguro desemprego: Após GRRF e cálculo da folha", "Selecione rescisões: Na tela \"Gerenciador de Folhas\"", "Envie ao Empregador Web: Clique \"Gerar arquivo\"", "Pessoal+", "Seguro-Desemprego", "Empregador Web"]
---

# Como gerar o arquivo do Seguro-Desemprego

**Módulo:** Pessoal+
**Caminho de Acesso:** Pessoal+ > Rotinas Folha > Gerenciador de Folhas > Gerar Arquivo para Seguro Desemprego
**ID da Tela:** br.com.sankhya.rh.GerenciadorFolha

---

## Descrição e Usabilidade

Após realizar a rescisão do trabalhador, transmitir os eventos ao eSocial e efetuar o recolhimento da Guia de Recolhimento Rescisório do FGTS - GRRF, é necessário gerar o arquivo do Seguro-Desemprego para envio ao portal [Empregador Web](https://sd.maisemprego.trabalho.gov.br/sdweb/empregadorweb/login.jsf).

O sistema permite gerar esse arquivo diretamente pelo [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247), utilizando as informações da folha rescisória já calculada.

O arquivo gerado será utilizado para importação no Empregador Web, permitindo que o empregador realize o requerimento do benefício do Seguro-Desemprego junto ao governo.

⚠️ A geração do arquivo não realiza o envio automático ao Empregador Web. Após gerar o arquivo, será necessário transmiti-lo manualmente no portal do governo.

### 1. Descrição da Funcionalidade

A funcionalidade de geração do arquivo do Seguro-Desemprego permite:

- gerar o arquivo para transmissão ao Empregador Web;
- selecionar funcionários desligados individualmente;
- emitir arquivos a partir das folhas rescisórias calculadas;
- centralizar o processo diretamente no Gerenciador de Folhas.

O sistema utiliza as informações da rescisão calculada para compor os dados obrigatórios do requerimento.

### 2. Pré-requisitos

Antes da geração do arquivo, é necessário:

- folha de rescisão calculada;
- rescisão validada;
- eventos transmitidos ao eSocial;
- recolhimento da GRRF realizado.

⚠️ Inconsistências cadastrais do trabalhador podem impedir a importação do arquivo no Empregador Web.

Recomenda-se validar previamente:

- CPF;
- PIS/PASEP;
- data de desligamento;
- categoria do trabalhador;
- motivo da rescisão.

### 3. Jornada de Uso

[GIF animado: Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/40468247532951)

1. Acesse a tela **Gerenciador de Folhas** (Pessoal+ > Rotinas Folha);
2. Utilize o painel de filtros para localizar a folha da Rescisão, informando:
   - **Empresa**;
   - **Referência**;
   - **Tipo de Folha** = **Rescisão**.
3. Clique em **Pesquisar**;
4. Clique sobre o card da rescisão;
5. Vá até a aba Folhas;
6. Acione a toogle **Ativa** **Seleção**, localizada no lado superior direito da tela;

   ⚠️ Com essa opção habilitada, o sistema permitirá selecionar individualmente os trabalhadores para geração do arquivo.
7. Marque os trabalhadores que devem compor o arquivo do Seguro-Desemprego;
8. Clique no botão **Gerar** **arquivo** **para** **Seguro** **Desemprego** e o sistema realizará a geração do arquivo;
9. Salve o arquivo em seu computador para enviar ao portal do Empregador Web.

   ![Imagem 2: Salve o arquivo em seu computador para enviar ao portal do Empregador Web.](https://ajuda.sankhya.com.br/hc/article_attachments/7080811463191)

⚠️ A transmissão ao governo ocorre fora do sistema Sankhya.

### 4. Pontos de Atenção

- O sistema somente gera o arquivo para trabalhadores com folha rescisória processada.
- Informações inconsistentes podem causar rejeição no Empregador Web.

  Valide principalmente:

  - CPF;
  - PIS;
  - datas;
  - categoria;
  - motivo da rescisão.
- Mesmo em folhas com múltiplas rescisões, os trabalhadores devem ser selecionados individualmente.
- Antes da geração do arquivo, recomenda-se:

  - transmitir os eventos rescisórios ao eSocial;
  - efetuar o recolhimento da GRRF.
- A geração do arquivo no sistema não realiza integração automática com o Empregador Web.
- O envio deve ser realizado manualmente no portal do governo.

## Artigos Relacionados

- [Geração da Guia de Recolhimento Rescisório do FGTS - GRRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/40469921798935)
- [Integração Financeira da Guia de Recolhimento Rescisório do FGTS - GRRF](https://ajuda.sankhya.com.br/hc/pt-br/articles/40475279854999)
- [Cálculos de Rescisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/5764158461847)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
- [Gerenciador de Folhas](https://ajuda.sankhya.com.br/hc/pt-br/articles/40106318532247)
