---
id: "39283751562007"
titulo: "Como resolver problemas de MDF-e não enviado à SEFAZ?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39283751562007-Como-resolver-problemas-de-MDF-e-n%C3%A3o-enviado-%C3%A0-SEFAZ"
trilha: "Melhores Práticas > Configurações"
atualizado_em: "2026-08-06T17:20:04Z"
rotulos: ["MDF-e", "Configuração", "XML", "SEFAZ", "Transporte", "Erro", "Artigo criado KCS", "Docs Eletrônicos - KCS", "Documentos Eletrônicos"]
---

# Como resolver problemas de MDF-e não enviado à SEFAZ?

O **Manifesto Eletrônico de Documentos Fiscais (MDF-e)** é um documento obrigatório para o transporte de mercadorias. Quando o MDF-e não é autorizado pela SEFAZ, o problema pode estar relacionado a configurações do sistema, pendências no manifesto ou validações realizadas pela própria SEFAZ.

Neste artigo, apresentamos as principais causas e como solucioná-las.

### **(1)** Verifique se o envio está configurado para o modo síncrono

Para emissões realizadas a partir de **01/07/2024**, a SEFAZ exige que o envio do XML do MDF-e seja realizado em **modo síncrono**. Configure esta opção seguindo os passos abaixo:

**(1)**Acesse a tela **"Empresa"** (Comercial Preferências Empresa).

**(2)**Clique na aba **"MDF-e"**.

**(3)**Ative o campo **"Usar modo síncrono para envio do XML"**. Salve as alterações.

### **(1)** Rejeição 611: MDF-e não encerrado

###

A rejeição ocorre quando já existe um **MDF-e em aberto** para a mesma:

- Placa do veículo;
- Tipo de emitente;
- UF de descarregamento.

Essa validação é realizada pela própria **SEFAZ**.

### Como resolver

Localize o MDF-e anterior e realize o seu encerramento antes de emitir um novo manifesto para o mesmo veículo.

**Importante:** enquanto o MDF-e anterior permanecer aberto, não será possível emitir outro manifesto nas mesmas condições.

### **(1)** Informações de pagamento de frete obrigatórias

Conforme a **Nota Técnica 2025.001 v1.02**, quando o transporte for realizado por **veículo de terceiros**, é obrigatório informar os dados de pagamento do frete.

**(1)**Acesse **Comercial > Arquivo > Cadastros > Viagens de Transporte (MDF-e)**.

**(2)**Clique na aba **"MDF-e"** e em seguida na sub-aba **"Pagamento Frete"**.

**(3)**Preencha todos os campos necessários:

- Forma de pagamento;
- Responsável pelo pagamento;
- Demais informações obrigatórias.
  **Observação:** caso a forma de pagamento seja **À vista**, não preencha a aba **Informações de pagamento a prazo**.

### **(1)** Erro 999: Erro não catalogado

O **Erro 999** é um retorno genérico da SEFAZ que normalmente indica instabilidade ou falha temporária no processamento do MDF-e.

- Aguarde alguns minutos.
- Tente realizar o envio novamente.
- Caso o erro persista, verifique a disponibilidade dos serviços da SEFAZ antes de abrir um chamado.

### **(1)** Verifique se os documentos fiscais estão autorizados

Somente **NF-e** e **CT-e** com situação **Autorizado** podem ser vinculados ao MDF-e.

Antes de gerar o manifesto:

- confirme se todas as NF-e ou CT-e foram autorizadas pela SEFAZ;
- caso exista algum documento rejeitado ou pendente, regularize-o antes de emitir o MDF-e.

### **(1)** Importância do encerramento do MDF-e

Após a conclusão da viagem, é obrigatório realizar o encerramento do manifesto.

Um MDF-e não encerrado pode impedir novas emissões para o mesmo veículo e gerar rejeições como a **611**.

### Como encerrar

1. Acesse **Comercial > Arquivo > Cadastros > Viagens de Transporte (MDF-e)**.
2. Localize o manifesto.
3. Utilize a opção **Encerrar MDF-e**.
