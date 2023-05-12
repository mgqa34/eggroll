package com.webank.eggroll.core.deepspeed.meta.store

import com.google.protobuf.ByteString
import com.webank.eggroll.core.meta.Deepspeed

import scala.language.implicitConversions

case class RendezvousStoreGetResponse(value: V)

object RendezvousStoreGetResponse {
  implicit def serialize(src: RendezvousStoreGetResponse): Array[Byte] = {
    val builder = Deepspeed.StoreGetResponse.newBuilder()
      .setValue(ByteString.copyFrom(src.value.toArray))
    builder.build().toByteArray
  }

  implicit def deserialize(byteString: ByteString): RendezvousStoreGetResponse = {
    val src = Deepspeed.StoreGetResponse.parseFrom(byteString)
    RendezvousStoreGetResponse(
      value = src.getValue.toByteArray.toVector
    )
  }
}