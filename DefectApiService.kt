package com.example.defectprediction.data.remote

import com.example.defectprediction.data.models.*
import retrofit2.Response
import retrofit2.http.*

interface DefectApiService {
    @POST("api/auth/register")
    suspend fun register(@Body request: AuthRequest): Response<AuthResponse>

    @POST("api/auth/login")
    suspend fun login(@Body request: AuthRequest): Response<AuthResponse>

    @GET("api/dashboard")
    suspend fun getDashboardStats(): Response<DashboardStatsDto>

    @POST("api/predictions/manual")
    suspend fun predictManual(@Body metrics: SoftwareMetricsDto): Response<PredictionResponse>

    @POST("api/predictions/batch")
    suspend fun predictBatch(@Body request: BatchPredictionRequest): Response<BatchPredictionResponse>

    @GET("api/predictions/history")
    suspend fun getPredictionHistory(): Response<List<PredictionResultDto>>

    @GET("api/model/info")
    suspend fun getModelInfo(): Response<Map<String, Any>>
}
