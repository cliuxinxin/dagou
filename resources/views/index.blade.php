@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
                    <table class="table table-striped">
                        <tr>
                            <th>招标</th>
                            <th>城市</th>
                            <th>开始日期</th>
                            <th>结束日期</th>
                        </tr>
                        @foreach($items as $item)
                            <tr>
                                <td><a href={{$item->url}}>{{str_limit($item->name, $limit = 65, $end = '...') }}</a></td>
                                <td>{{$item->city}}</td>
                                <td>{{$item->start_date}}</td>
                                <td>{{$item->end_date}}</td>
                            </tr>
                        @endforeach
                    </table>
        </div>
    {{ $items->links() }}
    </div>
</div>
@endsection
