package com.example.defectprediction.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.example.defectprediction.viewmodel.DefectViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DashboardScreen(
    viewModel: DefectViewModel,
    onNavigateToManual: () -> Unit,
    onNavigateToUpload: () -> Unit,
    onNavigateToResults: () -> Unit
) {
    val stats by viewModel.dashboardStats.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Defect Predictor", fontWeight = FontWeight.Bold) },
                colors = TopAppBarDefaults.topAppBarColors(
                    containerColor = MaterialTheme.colorScheme.primaryContainer
                )
            )
        }
    ) { padding ->
        LazyColumn(
            modifier = Modifier.fillMaxSize().padding(padding).padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(14.dp)
        ) {
            item {
                Row(modifier = Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                    Card(modifier = Modifier.weight(1f)) {
                        Column(modifier = Modifier.padding(14.dp)) {
                            Text("Total Modules", color = Color.Gray)
                            Text("${stats.totalModules}", style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold)
                        }
                    }
                    Card(modifier = Modifier.weight(1f)) {
                        Column(modifier = Modifier.padding(14.dp)) {
                            Text("Defective", color = Color.Gray)
                            Text("${stats.defectiveModules}", style = MaterialTheme.typography.headlineSmall, fontWeight = FontWeight.Bold, color = Color(0xFFDC2626))
                        }
                    }
                }
            }
            item {
                Button(onClick = onNavigateToUpload, modifier = Modifier.fillMaxWidth()) {
                    Text("Upload Dataset (CSV/Excel)")
                }
            }
            item {
                OutlinedButton(onClick = onNavigateToManual, modifier = Modifier.fillMaxWidth()) {
                    Text("Manual Metric Calculator")
                }
            }
        }
    }
}
