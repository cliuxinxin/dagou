<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class GroupDetail extends Model
{
    //
    protected $guarded = [];

    /**
     * A group detail belong to a group
     *
     * @return \Illuminate\Database\Eloquent\Relations\BelongsTo
     */
    public function group()
    {
        return $this->belongsTo('App\Group');
    }

}
