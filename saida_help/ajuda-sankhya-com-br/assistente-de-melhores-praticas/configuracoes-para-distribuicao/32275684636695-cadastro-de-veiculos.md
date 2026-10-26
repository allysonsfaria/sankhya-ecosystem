---
id: "32275684636695"
titulo: "Cadastro de Veículos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32275684636695-Cadastro-de-Ve%C3%ADculos"
trilha: "Assistente de Melhores Práticas > Configurações para Distribuição"
atualizado_em: "2026-07-22T16:16:32Z"
rotulos: ["Configuração", "Veículos", "Parceiro", "Transporte", "Cadastro"]
---

# Cadastro de Veículos

### Descrição

#### Gestão de Veículos

Registra e atualiza informações de veículos da frota, garantindo mais segurança e eficiência nas operações de transporte.

#### Gestão e Configuração de Veículos

- **Gestão de Veículos:** Permite consultar, cadastrar e editar os veículos utilizados no controle de distribuição.
- **Configuração de Veículos:** Garante o monitoramento de informações essenciais, como quilometragem, gastos com manutenção, horários de saída e entrada, entre outros.

### Como instalar

1. Clique em **"Iniciar"**.

2. Selecione os **grupos de usuários** ou **usuários** responsáveis pelo cadastro de veículos.

3. Clique em **"Avançar"**.

4. Preencha os campos do formulário com as seguintes informações do veículo:

- Placa de matrícula
- CNPJ/CPF do proprietário
- Cidade do registro
- RNTRC
- RENAVAN
- Marca/Modelo
- Peso máximo (kg)
- Volume máximo (m³)
- Ano de fabricação
- Ano do modelo
- Cor
- Chassi
- Tipo de combustível

5. Clique em **"Salvar"** (ícone de disquete) e em **"Avançar"**.

6. Se o proprietário for pessoa física, complete o cadastro como parceiro.

7. Se o proprietário for pessoa jurídica, confira as informações do cadastro como parceiro.

8. Verifique o resumo da configuração do Cadastro do Veículo.

9. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da instalação

Se o condutor do veículo **não for um parceiro cadastrado**, o sistema verifica se o **CEP inserido** já está registrado. Caso contrário, a atualização ocorre sequencialmente nas seguintes tabelas:

1. **Cadastro de Endereço** (caso ainda não esteja registrado)

   - TSITEND – Tipo de endereço
   - TSIEND – Endereço
   - TSIBAI – Bairro
   - TSICID – Cidade
2. **Outras Tabelas Atualizadas**

   - TGFPAR – Cadastro de parceiros
   - TGFVEI – Cadastro de veículos
   - TDDPER – Acesso à tela de veículo

### Como simular

Para acessar os cadastros realizados:

Veículos:

1. vá até Configurações > Cadastros > Veículos.
2. clique em "**Mostrar grade**" e em "**Atualizar**".

**Vale saber**

Vai cadastrar veículos? Capriche nas informações — cada detalhe conta na hora de controlar custos, planejar rotas e garantir conformidade. E lembre-se: se o proprietário ou condutor ainda não estiver cadastrado como parceiro, o sistema cuida disso automaticamente. É só seguir o fluxo!
