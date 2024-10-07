# **Sistema de Apoio à Decisão para Análise de Vendas e Comissão**

### **1. Introdução**
Este projeto visa desenvolver um Sistema de Apoio à Decisão (SAD) utilizando o Microsoft Fabric para fins de demonstração da plataforma.

**Use Case**: Análise de dados de vendas de uma empresa fictícia do setor do agronegócio.

### **2. Objetivo**
Desenvolver um pipeline end-to-end no Microsoft Fabric para consolidar dados de vendas e cadastros, calcular comissões e fornecer insights valiosos por meio de visualizações dinâmicas no Power BI.

### **3. Arquitetura do Sistema**

#### **Visão Geral da Arquitetura**

![Arquitetura do Projeto](assets/data%20stack_oficina_pucminas.png)

- **Fontes de Dados:**
  - **API**: Responsável por fornecer os dados de vendas em tempo real.
  - **Postgres**: Contém os dados de cadastro de clientes, produtos, filiais, vendedores e gerentes.
  
- **Processo de Ingestão:**
  - O processo de ingestão é realizado por **Spark Notebooks** que capturam dados das duas fontes (API e Postgres) e os armazenam na **Raw Zone** para processamento inicial.

- **Armazenamento (OneLake)**:
  - **Raw Zone**: Armazena os dados brutos, sem tratamento.
  - **Trusted Zone**: Armazena os dados processados e limpos, prontos para transformação.
  - **Refined Zone**: Contém os dados transformados e preparados para análises e geração de relatórios.
  
- **Transformação dos Dados**:
  - A transformação é realizada em **Spark Notebooks**, aplicando regras de negócio e cálculos de comissão, como 2% de comissão para vendedores e 0.8% para gerentes, além de outras validações.

- **Orquestração**:
  - **Pipelines** garantem a execução automática e agendada de todo o fluxo de ingestão, transformação e carga de dados, integrando os módulos do Microsoft Fabric.

- **Visualização de Dados e Análise**:
  - **Warehouse ([TDS](https://learn.microsoft.com/pt-br/sql/relational-databases/security/networking/tds-8?view=sql-server-ver16) Endpoint)**: Os dados refinados são armazenados para análise e visualização no Power BI.
  - **Power BI**: Utilizado para criar dashboards interativos, com KPIs como total de vendas, comissão de vendedores e gerentes, e comparações entre filiais e períodos.

---

### **4. Fluxo do Processo End-to-End**

1. **Ingestão de Dados**:
   - Extração de dados de vendas da API em tempo real e dos cadastros armazenados no banco de dados Postgres.
   
2. **Processamento e Transformação**:
   - Limpeza dos dados e cálculo automático de comissões.
   - Consolidação dos dados na **Trusted Zone** e aplicação de regras de negócio.
   
3. **Armazenamento**:
   - Dados limpos e consolidados são armazenados na **Refined Zone**.
   
4. **Visualização e Relatórios**:
   - Os dados refinados são carregados no Power BI para visualização em dashboards dinâmicos.

---

### **5. KPIs e Métricas Monitoradas**

- **Faturamento por Filial**
- **Comissão dos Vendedores**
- **Comissão dos Gerentes**
- **Vendas por Produto**
- **Meta versus Realizado (Vendas)**
- **Comparação de Desempenho entre Filiais**

---

### **6. Benefícios Esperados**

- **Automação Total**: Automatização do cálculo de comissões e ingestão de dados, reduzindo erros manuais.
- **Escalabilidade**: O sistema é escalável, podendo lidar com grandes volumes de dados e integração com novas fontes no futuro.
- **Visualização de Insights**: A integração com Power BI permite a visualização em tempo real das vendas e comissões, proporcionando uma melhor gestão e acompanhamento de metas.
- **Governança e Segurança**: Controle total do acesso aos dados e rastreabilidade das alterações através de logs.

---

### **7. Extensões Futuras**

- **Integração com ERP**: Conectar o sistema com ERP para sincronização de dados em tempo real.
- **Análise Preditiva**: Adicionar modelos de machine learning para previsão de vendas e desempenho futuro com base nos dados históricos.
- **Alertas e Notificações**: Implementar alertas automáticos para informar metas alcançadas ou variações inesperadas nas vendas.

---

### **8. Conclusão**

Este projeto propõe uma solução moderna, automatizada e escalável para a análise de vendas e cálculo de comissões no setor do agronegócio. Utilizando o poder do Microsoft Fabric e Power BI, fornecemos uma plataforma robusta que facilita a tomada de decisões e melhora a eficiência no monitoramento de vendas e gestão de equipes.
