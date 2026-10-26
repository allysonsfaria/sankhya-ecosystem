---
id: "42430466054423"
titulo: "Componente Anexo"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42430466054423-Componente-Anexo"
trilha: "NEPPO: Personalização de atendimento > Construtor de bot"
atualizado_em: "2026-08-11T16:07:02Z"
rotulos: ["sync_hc", "neppo", "neppo_858000342", "sync_hash_3c601568c6e4"]
---

# Componente Anexo

O componente **Anexo** envia um arquivo ao usuário dentro do fluxo do bot — imagem, documento, áudio ou vídeo — com legenda opcional.

---

## Visão geral

Use o Anexo quando o bot precisar compartilhar conteúdo em arquivo: catálogos em PDF, imagens de produtos, comprovantes, áudios explicativos, vídeos institucionais etc.

Diferente do componente **Texto** (que aceita arquivo apenas por URL externa), o Anexo trabalha com o upload do arquivo diretamente na configuração do componente.

---

## Localização

Paleta de componentes (menu lateral direito da Área do Construtor) → categoria **Elementos** → **Anexo**.

---

## Campos de configuração

| Campo | Obrigatório | Descrição | Exemplo |
| --- | --- | --- | --- |
| Arquivo | Sim | Arquivo a ser enviado ao usuário. Tamanho máximo: **15 MB** | `catalogo-cursos.pdf` |
| Legenda | Não | Texto que acompanha o arquivo. Aceita `{{variavel}}` | `Segue o catálogo de cursos, {{contact.displayName}}!` |

---

## Comportamento

- O arquivo é enviado ao usuário e o fluxo **segue imediatamente** para o próximo componente (não há espera por resposta).
- A renderização depende do canal: no WhatsApp, imagens e vídeos aparecem com pré-visualização e a legenda junto do arquivo; documentos aparecem como anexo para download.
- A legenda aceita interpolação de variáveis com a sintaxe `{{variavel}}`.

---

## Exemplo real de uso

A jornada de matrícula escolar analisada nesta documentação não utiliza o componente Anexo — o compartilhamento de links (ex.: página de vagas do "Trabalhe conosco") foi feito via componente **Texto** com URL no corpo da mensagem.

Um uso típico do Anexo nesse mesmo cenário seria enviar o **catálogo de cursos em PDF** logo após o usuário escolher o curso de interesse no menu:

- Arquivo: `catalogo-anos-iniciais.pdf`
- Legenda: `Aqui está o material do curso {{Curso}} para o ano letivo {{AnoLetivo}} 📚`

---

## Boas práticas e limitações

- **Limite de 15 MB por arquivo** — comprima PDFs e vídeos antes do upload.
- Verifique os formatos suportados pelo canal de destino (o WhatsApp, por exemplo, possui restrições próprias de tipo e tamanho de mídia).
- Use a legenda para contextualizar o arquivo em vez de enviar um Texto separado.
- Para arquivos hospedados externamente (URLs dinâmicas vindas de API), utilize o componente **Texto** com arquivo por URL.
- Evite enviar vários anexos em sequência sem pausa — pode poluir a conversa e gerar bloqueios do canal.
