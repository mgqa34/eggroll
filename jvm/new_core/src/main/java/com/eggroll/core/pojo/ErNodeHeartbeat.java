package com.eggroll.core.pojo;


import com.webank.eggroll.core.meta.Meta;
import lombok.Data;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Data
public class ErNodeHeartbeat implements RpcMessage {
    Logger log = LoggerFactory.getLogger(ErNodeHeartbeat.class);
    private long id;
    private ErServerNode node;

    public ErNodeHeartbeat() {
        this.id = -1;
        this.node = null;
    }

    public ErNodeHeartbeat(long id, ErServerNode node) {
        this.id = id;
        this.node = node;
    }


    @Override
    public String toString() {
        return "<ErNodeHeartbeat(id=" + id + ", node=" + node +
                ") at " + Integer.toHexString(hashCode()) + ">";
    }

    public Meta.NodeHeartbeat toProto() {
        Meta.NodeHeartbeat.Builder builder = Meta.NodeHeartbeat.newBuilder();
        builder.setId(this.id)
                .setNode(this.node.toProto());
        return builder.build();
    }

    public static ErNodeHeartbeat fromProto( Meta.NodeHeartbeat nodeHeartbeat){
        ErNodeHeartbeat erNodeHeartbeat = new ErNodeHeartbeat();
        erNodeHeartbeat.deserialize(nodeHeartbeat.toByteArray());
        return erNodeHeartbeat;
    }

    @Override
    public byte[] serialize() {
        return toProto().toByteArray();
    }

    @Override
    public void deserialize(byte[] data) {
        try {
            Meta.NodeHeartbeat nodeHeartbeat = Meta.NodeHeartbeat.parseFrom(data);
            this.id = nodeHeartbeat.getId();
            ErServerNode erServerNode = new ErServerNode();
            erServerNode.deserialize(nodeHeartbeat.getNode().toByteArray());
            this.node = erServerNode;
        } catch (Exception e) {
            log.error("deserialize error : ", e);
        }
    }
}