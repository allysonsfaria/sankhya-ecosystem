---
id: "37945484046615"
titulo: "Como realizar a manifestação de destinatário em documento fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37945484046615-Como-realizar-a-manifesta%C3%A7%C3%A3o-de-destinat%C3%A1rio-em-documento-fiscal"
trilha: "Universidade Sankhya > Jornada de Manifestação de Destinatário (MD-e)"
atualizado_em: "2026-08-18T12:30:01Z"
rotulos: ["Configuração", "Fiscal", "NF-e", "XML", "SEFAZ", "Documentos Eletrônicos"]
---

# Como realizar a manifestação de destinatário em documento fiscal

## Manifestação de destinatário em documentos fiscais

#### Como a manifestação fortalece a governança fiscal?

- **Comprovação oficial e prevenção de fraudes.**

A manifestação registra, na SEFAZ, a posição do destinatário sobre a NF-e (reconhecida, desconhecida, recusada ou ciência). Esse registro evita vinculações indevidas do CNPJ e bloqueia o uso em operações fraudulentas. É importante lembrar que, após a Ciência da Operação, a empresa possui 180 dias para registrar uma manifestação conclusiva (Confirmação, Desconhecimento ou Operação não Realizada), prazo definido pela SEFAZ e sujeito a alterações.

- **Acesso oficial ao XML e governança tributária.**

A Ciência ou Confirmação viabiliza o download do XML, insumo obrigatório para escrituração, conferência, auditorias e integrações fiscais. Com XML íntegro, a empresa sustenta créditos (ICMS/PIS/COFINS), evita não reconhecimento desses créditos e mantém rastreabilidade para obrigações acessórias.

- **Integridade de dados e eficiência no ERP.**

A manifestação contribui para a integridade das informações que chegam ao ERP, pois estabelece quais documentos são oficialmente reconhecidos pela empresa. Esse alinhamento favorece a consistência de dados fiscais, o cálculo correto de custos, a confiabilidade dos saldos de estoque e a redução de inconsistências em rotinas de compras e recebimento. Além disso, a automação de etapas como consulta, ciência e download de XML amplia a eficiência, diminuindo intervenções manuais e otimizando fluxos internos.

- **Rastreabilidade e orquestração entre áreas.**

Os eventos de manifestação criam um histórico auditável do ciclo do documento, fortalecendo controles internos e atendimentos a fiscalizações. Esse processo também alinha Compras, Fiscal, Logística e Contábil, garantindo o “triple-check” (pedido → NF-e → recebimento) e diminuindo custos de correção.

**É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya**

**Atenção**

Siga as orientações indicadas no passo a passo e observe a demonstração prática no sistema para reforçar o aprendizado do processo. 

**Importante**
Para a execução desta atividade, é necessário criar um pedido de compra: um o fornecedor **Real Alimentos e Distribuição**, com **720 unidades** do produto **Feijão Carioca - 1 Kg**.

Caso não possua os cadastros em sua base de testes, adapte o XML seguindo as orientações da preparação dessa jornada. 

1. **Importe o XML e valide o documento**

- Siga as orientações do Script de Configuração acima para importação manual do documento fiscal 
  Essa etapa corresponde à simulação do exercício na jornada. Em ambiente operacional, o registro é disponibilizado automaticamente após a consulta realizada na rotina Configuração MD-e/DF-e.

2. **Para manifestações via Portal de Importação de XML**

**Menu:** Comercial » Rotinas » Portal de Importação de XML 

- Selecione o registro do documento na grade de resultados
- Clique no botão “MD-e” e selecione o evento adequado para a sua necessidade

**Em caso de recusa, siga os passos:**

- Selecione o XML que será recusado
- Acione o botão MD-e, opção "Operação não realizada";
- No pop-up apresentado, detalhe a justificativa da recusa e conclua a ação

![Imagem 1: No pop-up apresentado, detalhe a justificativa da recusa e conclua a ação](https://ajuda.sankhya.com.br/hc/article_attachments/37945484027287)

**Atenção!**

- A base de treinamento opera em modo de homologação e não possui certificado digital válido, portanto não será possível enviar eventos de manifestação.
- Para que a manifestação do documento seja indicada, a nota deve estar com confirmação pendente.
- Para visualizar o modelo de impressão dos documentos importados acesse botão **MD-e > Visualizar NF-e/CT-e**

3. **Para manifestações via Central de Compras**

- Na tela Portal de Importação de XML selecione o registro desejado e clique em “**Abrir Documento**”
- Ao ser direcionado para a tela Central de Compras, no menu principal clique no botão “**MD-e**”
- Selecione o evento adequado à sua necessidade  
  Ex.: Ciência da operação
- Após registrar a manifestação, confirme a nota.

![Imagem 2: Após registrar a manifestação, confirme a nota.](https://ajuda.sankhya.com.br/hc/article_attachments/37945484032279)
