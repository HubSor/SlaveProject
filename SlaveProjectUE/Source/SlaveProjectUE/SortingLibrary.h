// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "Kismet/BlueprintFunctionLibrary.h"
#include "SortingLibrary.generated.h"

/**
 * 
 */

USTRUCT(BlueprintType)      // Define custom struct and expose to blueprints
struct Initiative          // This will be the name of the new struct in BPs 
{

    GENERATED_USTRUCT_BODY()

public:

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Actor Distance")    // allow this property to be edited in BPs
        float distance = 0;

    UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Actor Distance")    // allow this property to be edited in BPs
        AActor* actor = NULL;

};

UCLASS()
class SLAVEPROJECTUE_API USortingLibrary : public UBlueprintFunctionLibrary
{
	GENERATED_BODY()
	
public:

    UFUNCTION(BlueprintCallable, Category = "Sorting Functions")    // Sort actors by distance from target actor    
        static void  Initiative_Sort(UPARAM() TArray <AActor*> Array_To_Sort, UPARAM()AActor* From_Actor, bool Descending, TArray <Initiative>& Sorted_Array);
};
