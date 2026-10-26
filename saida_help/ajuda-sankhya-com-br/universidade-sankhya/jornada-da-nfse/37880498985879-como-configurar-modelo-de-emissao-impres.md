---
id: "37880498985879"
titulo: "Como configurar modelo de emissão/impressão de RPS e NFSe"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37880498985879-Como-configurar-modelo-de-emiss%C3%A3o-impress%C3%A3o-de-RPS-e-NFSe"
trilha: "Universidade Sankhya > Jornada da NFSe"
atualizado_em: "2026-07-22T14:06:31Z"
rotulos: ["Configuração", "Impressão", "XML", "Prefeituras", "NFS-e", "RPS"]
---

# Como configurar modelo de emissão/impressão de RPS e NFSe

## Modelo de emissão/impressão de RPS e NFSe

Ao configurar a NFS-e no ERP Sankhya, você precisa escolher o modelo de emissão/impressão que será adotado. Esse modelo define como a nota será transmitida à prefeitura e também como ficará disponível para consulta.

Na prática, existem duas possibilidades:

- **Emissão direta de NFS-e:**  a nota é enviada imediatamente para a prefeitura e já retorna com validade fiscal.
- **Emissão via RPS (Recibo Provisório de Serviços):** funciona como uma pré-nota, utilizada no momento da prestação. O RPS precisa ser convertido em NFS-e oficial dentro do prazo definido pelo município para ter validade jurídica.

Ao vincular o modelo correto, você garante que o processo siga as exigências da prefeitura e que a nota esteja organizada de forma clara, pronta para uso interno e para o cliente.

#### Siga as orientações para realizar a configuração no ERP Sankhya

**Atenção!** A base utilizada na capacitação do Backoffice já vem habilitada com essa configuração.

1. Acesse a tela **Modelo de Impressão (Nota/Pedido)**

**Menu:** Comercial » Arquivo » Cadastros » Modelo de Impressão (Nota/Pedido)

- Clique no botão “**+**” (**Cadastrar Relatório**)
- No campo **Descrição**, informe o nome do modelo
  Ex. RPS (cidade); NFS-e (cidade).
- Salve o registro.
- Acesse a aba Arquivos para adicionar o arquivo XML do modelo de impressão adotado pela cidade da empresa.

2. Acesse a tela **Modelos de Nota Fiscal/Duplicatas/Boleto(s)**

**Menu:** Configurações » Avançado » Modelos de Nota Fiscal/Duplicatas/Boleto(s)

- Clique em **+ Novo registro**
- No campo indicado informe o nome do modelo
  Ex. RPS (cidade); NFS-e (cidade).
- No campo **Tipo de impressora**, selecione a opção “**Outras**”
- Informe “**?**” no campo **Caminho**
- No campo **Número do relatório modelo** selecione o código do modelo criado no passo anterior
- Salve o registro
